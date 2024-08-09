"""empty message

Revision ID: 690d1c3fe3ab
Revises: 676ba474c351
Create Date: 2024-03-16 19:34:58.651713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '690d1c3fe3ab'
down_revision = '676ba474c351'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('director', sa.String(), nullable=True),
    sa.Column('avg_rating', sa.Float(), nullable=True),
    sa.Column('ticket_price', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Movie')
    # ### end Alembic commands ###